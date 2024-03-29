# -*- coding: utf-8 -*-
"""
Webサーバ３台とDatabaseサーバ１台により構成されたWebサービスがある。
サービスの運用状況を調査したところ、Webサーバの稼働率(※)は平均で45%であり、
ピーク時には60%であった。また、Databaseサーバの稼働率は平均で30%であり、
ピーク時には50%であった。なお、WebサーバとDatabaseサーバの負荷状況はほぼ
一致しておりピーク時間帯にずれはなかった。
                
以上の条件から以下の問いに答えて下さい。
上記の条件が不十分で問いに合理的な回答ができない場合には、必要な条件を仮定してください。
                        
※ 稼働率の上限は100%、それ以上に処理量が増加するとサーバがダウンしシステムが破綻する。
（１）サーバ台数を維持したままでこのままサービスを提供する場合、現在の何倍までの利用者数増加に耐えられるか。
    1.8倍までの利用者数増加まで耐えられます。

（２）Databaseサーバが1台のままだとして、Webサーバはあと何台増設できるか。
    3台増設するのができます。

（３）Webサーバの台数を３台から２台に減らす事にしました。この場合のメリットとデメリットをあげてください。
    メリットは Databaseサーバの稼働率は平均30%が20%に下がり、ピーク時には50%が35%ぐらいまで下がります。
    デメリットは Webサーバの稼働率は平均45%が67%にあがり、ピーク時は60%が90%になります。
（４）現在のシステム構成に問題があれば指摘してください。
    WebサーバーとDatabaseサーバーを一台ずつ増やす。
    理由:
        現在Webサーバーの稼働率は平均45%でビック時には50%超えているので、
        注意信号がずっとついている状態だと思っております。
        1台増やすによって、平均45%が30%ぐらいになり、ピック時も60%が40%ぐらいになりながら、
        webサーバーが安定になるとおもっております。。
        またWebサーバーの増設によってDatabaseサーバの稼働率はもっとあがりますので、
        1台増設によって半分減らして、もっと効率になります。

"""
