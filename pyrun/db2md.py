#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
import sys
import os
import argparse
from datetime import datetime

class MySQLToMarkdownExporter:
    def __init__(self, host='localhost', user='root'):
        self.host = host
        self.user = user
        self.password = os.getenv('MYSQL_PASSWORD')
        
        if not self.password:
            raise ValueError("请设置 MYSQL_PASSWORD 环境变量")
    
    def export_data(self, database, table, output_file):
        """从MySQL导出数据到Markdown格式文件"""
        
        try:
            # 连接到数据库
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=database
            )
            
            cursor = connection.cursor(dictionary=True)
            
            # 查询数据，按prefix分组
            query = f"SELECT prefix, description, body FROM {table} ORDER BY prefix, description"
            cursor.execute(query)
            
            data = cursor.fetchall()
            
            if not data:
                print("警告: 未找到有效数据")
                return
            
            # 组织数据：按prefix分组
            grouped_data = {}
            for row in data:
                prefix = row['prefix']
                description = row['description']
                body = row['body']
                
                if prefix not in grouped_data:
                    grouped_data[prefix] = []
                
                grouped_data[prefix].append({
                    'description': description,
                    'body': body
                })
            
            # 写入Markdown文件
            with open(output_file, 'w', encoding='utf-8') as f:
                # 写入文件标题
                f.write(f"# {table.capitalize()} 记录\n\n")
                f.write(f"导出时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # 遍历每个prefix（二级标题）
                for prefix, items in grouped_data.items():
                    # 写入二级标题
                    f.write(f"## {prefix}\n\n")
                    
                    # 遍历每个description（三级标题）
                    for item in items:
                        description = item['description']
                        body = item['body']
                        
                        # 写入三级标题
                        f.write(f"### {description}\n\n")
                        
                        # 写入内容，处理换行
                        if body:
                            # 将数据库中的换行符转换为Markdown换行
                            formatted_body = body.replace('\\n', '\n\n')
                            f.write(f"{formatted_body}\n\n")
                        else:
                            f.write("（无内容）\n\n")
            
            print(f"导出完成！总共导出 {len(data)} 条记录到 {output_file}")
            
            # 显示导出的数据统计
            print("\n导出的数据统计:")
            print("-" * 40)
            print(f"总记录数: {len(data)}")
            print(f"不同的prefix数量: {len(grouped_data)}")
            
            # 显示分组预览
            print("\n分组预览:")
            print("-" * 40)
            for prefix, items in list(grouped_data.items())[:5]:  # 显示前5个分组
                print(f"## {prefix} ({len(items)} 条记录)")
                for item in items[:3]:  # 每个分组显示前3条
                    print(f"  ### {item['description'][:30]}...")
                if len(items) > 3:
                    print(f"  ... 还有 {len(items)-3} 条")
                print()
            
            return len(data)
            
        except Exception as e:
            print(f"导出失败: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()

def main():
    parser = argparse.ArgumentParser(description='从MySQL数据库导出数据到Markdown格式文件')
    parser.add_argument('database', help='数据库名称')
    parser.add_argument('table', help='表名称')
    parser.add_argument('output_file', help='输出文件路径')
    parser.add_argument('--host', default='localhost', help='MySQL主机地址')
    parser.add_argument('--user', default='root', help='MySQL用户名')
    
    args = parser.parse_args()
    
    try:
        exporter = MySQLToMarkdownExporter(host=args.host, user=args.user)
        exporter.export_data(args.database, args.table, args.output_file)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
