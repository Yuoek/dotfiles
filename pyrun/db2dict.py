#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
import sys
import os
import argparse
from datetime import datetime

class MySQLToDictExporter:
    def __init__(self, host='localhost', user='root'):
        self.host = host
        self.user = user
        self.password = os.getenv('MYSQL_PASSWORD')
        
        if not self.password:
            raise ValueError("请设置 MYSQL_PASSWORD 环境变量")
    
    def export_data(self, database, table, output_file):
        """从MySQL导出数据到字典格式文件"""
        
        try:
            # 连接到数据库
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=database
            )
            
            cursor = connection.cursor(dictionary=True)
            
            # 查询数据
            query = f"SELECT prefix, description FROM {table} ORDER BY prefix"
            cursor.execute(query)
            
            data = cursor.fetchall()
            
            if not data:
                print("警告: 未找到有效数据")
                return
            
            # 处理数据：将description按空格分割，为每个部分创建独立的行
            processed_data = []
            for row in data:
                prefix = row['prefix']
                description = row['description']
                
                # 按空格分割description
                if description:
                    parts = description.split()
                    for part in parts:
                        if part:  # 跳过空字符串
                            processed_data.append({
                                'prefix': prefix,
                                'description': part
                            })
            
            # 写入文件
            with open(output_file, 'w', encoding='utf-8') as f:
                for item in processed_data:
                    f.write(f"{item['description']}\t{item['prefix']}\n")
            
            print(f"导出完成！总共导出 {len(processed_data)} 条记录到 {output_file}")
            
            # 显示导出的数据预览
            print("\n导出的数据预览:")
            print("-" * 40)
            print(f"{'prefix':<10} | {'description':<20}")
            print("-" * 40)
            for item in processed_data[:10]:  # 显示前10条记录
                print(f"{item['prefix']:<10} | {item['description']:<20}")
            
            return len(processed_data)
            
        except Exception as e:
            print(f"导出失败: {e}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()

def main():
    parser = argparse.ArgumentParser(description='从MySQL数据库导出数据到字典格式文件')
    parser.add_argument('database', help='数据库名称')
    parser.add_argument('table', help='表名称')
    parser.add_argument('output_file', help='输出文件路径')
    parser.add_argument('--host', default='localhost', help='MySQL主机地址')
    parser.add_argument('--user', default='root', help='MySQL用户名')
    
    args = parser.parse_args()
    
    try:
        exporter = MySQLToDictExporter(host=args.host, user=args.user)
        exporter.export_data(args.database, args.table, args.output_file)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
