# -*- coding: utf-8 -*-
"""
DBサーバのメモリチューニングについての問題です。
メモリが24G搭載されているマシンとします。
innoDBのデータサイズは12G、瞬間接続数の平均は600とします。
下記値以外のメモリ使用量を1Gとしたとき、
安全にDBサーバを運用するために、下記数値は問題があるでしょうか？
あるとすればあなたならどのようにチューニングしますか？

    sort_buffer_size                = 4M
    read_buffer_size                = 4M
    read_rnd_buffer_size            = 4M
    myisam_sort_buffer_size         = 1M
    query_cache_size                = 256M
    max_connections                 = 1000
    thread_cache_size               = 1000
    tmp_table_size                  = 256M
    max_heap_table_size             = 256M
    query_cache_limit               = 256M
    innodb_buffer_pool_size         = 16G
    innodb_additional_mem_pool_size = 20M
    innodb_log_file_size            = 512M
    innodb_log_buffer_size          = 16M
"""
"""
回答:
    1)
        read_buffer_size = 1MB 
        理由:パフォーマンスを考えるならば、
            インデックスを使うようなクエリを発行するべきなので、
            4MBまで増やす必要はありません。
    2)
        read_rnd_buffer_size = 2M
        理由:スレッドバッファなので、割り当て過ぎには注意が必要です。
            最大2Mまで設定しても大丈夫と判断します。
    3)
        query_cache_limit = 20M
        理由:query_cache_sizeと同じサイズに設定するとキャッシュー範囲が
            増えてしまい、逆にパフォーマンスが下がります。
        
"""
