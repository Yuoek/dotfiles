#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import mysql.connector
import sys
import os
import argparse
from datetime import datetime

class MarkdownToMySQLImporter:
    def __init__(self, host='localhost', user='root'):
        self.host = host
        self.user = user
        self.password = os.getenv('MYSQL_PASSWORD')
        
        if not self.password:
            raise ValueError("请设置 MYSQL_PASSWORD 环境变量")
    
    def parse_markdown(self, md_file):
        """解析Markdown文件，提取二级标题、三级标题和内容"""
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用正则表达式匹配模式
        # 匹配二级标题 (##) 和三级标题 (###) 以及它们之间的内容
        pattern = r'##\s*(.+?)\s*\n###\s*(.+?)\s*\n(.*?)(?=\n##|\Z)'
        
        matches = re.findall(pattern, content, re.DOTALL)
        
        data = []
        for match in matches:
            prefix = match[0].strip()
            description = match[1].strip()
            body = match[2].strip()
            
            # 清理body内容，移除多余的空白字符但保留格式
            body_lines = []
            for line in body.split('\n'):
                line = line.rstrip()  # 只移除右侧空白
                if line:  # 保留空行
                    body_lines.append(line)
            
            body = '\n'.join(body_lines)
            
            data.append({
                'prefix': prefix,
                'description': description,
                'body': body
            })
        
        return data
    
    def import_data(self, database, table, md_file, batch_size=100000):
        """批量导入数据"""
        
        try:
            # 解析Markdown文件
            data = self.parse_markdown(md_file)
            
            if not data:
                print("警告: 未找到有效数据")
                return
            
            # 连接到数据库
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=database
            )
            
            cursor = connection.cursor()
            
            # 准备SQL语句
            insert_query = f"""
            INSERT INTO {table} (prefix, description, body)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            description = VALUES(description),
            body = VALUES(body)
            """
            
            # 批量插入数据
            batch_data = []
            success_count = 0
            
            for item in data:
                prefix = item.get('prefix', '')
                description = item.get('description', '')
                body = item.get('body', '')
                
                if prefix:  # 确保有主键
                    batch_data.append((prefix, description, body))
                    
                    # 达到批量大小或最后一条记录时执行插入
                    if len(batch_data) >= batch_size:
                        cursor.executemany(insert_query, batch_data)
                        success_count += len(batch_data)
                        batch_data = []
                        print(f"已导入 {success_count} 条记录...")
            
            # 插入剩余记录
            if batch_data:
                cursor.executemany(insert_query, batch_data)
                success_count += len(batch_data)
            
            connection.commit()
            
            print(f"\n导入完成！总共导入 {success_count} 条记录")
            
            # 显示导入的数据预览
            print("\n导入的数据预览:")
            print("-" * 80)
            print(f"{'prefix':<10} | {'description':<20} | {'body (前50字符)':<50}")
            print("-" * 80)
            for item in data[:5]:  # 显示前5条记录
                body_preview = item['body'][:50] + "..." if len(item['body']) > 50 else item['body']
                print(f"{item['prefix']:<10} | {item['description']:<20} | {body_preview:<50}")
            
        except Exception as e:
            print(f"导入失败: {e}")
            if 'connection' in locals():
                connection.rollback()
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()

def main():
    parser = argparse.ArgumentParser(description='将Markdown数据导入MySQL数据库')
    parser.add_argument('database', help='数据库名称')
    parser.add_argument('table', help='表名称')
    parser.add_argument('md_file', help='Markdown文件路径')
    parser.add_argument('--host', default='localhost', help='MySQL主机地址')
    parser.add_argument('--user', default='root', help='MySQL用户名')
    parser.add_argument('--batch-size', type=int, default=100, help='批量插入大小')
    
    args = parser.parse_args()
    
    try:
        importer = MarkdownToMySQLImporter(host=args.host, user=args.user)
        importer.import_data(args.database, args.table, args.md_file, args.batch_size)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
