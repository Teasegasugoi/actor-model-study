# 以下のURL先コードをそのまま使用しています
# https://blog.amedama.jp/entry/2017/03/14/005610

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import time

import pykka


class MyActor(pykka.ThreadingActor):

    def process(self, processing_id, sleep_sec):
        """時間がかかる処理を模したメソッド"""
        time.sleep(sleep_sec)
        print('Completed: ID {0} in {1} s'.format(processing_id, sleep_sec))


def main():
    actor_proxy_a = MyActor.start().proxy()
    actor_proxy_b = MyActor.start().proxy()

    start_time = time.time()

    future1 = actor_proxy_a.process(1, 1)
    future2 = actor_proxy_a.process(2, 1)

    future3 = actor_proxy_b.process(3, 1)
    future4 = actor_proxy_b.process(4, 1)

    future1.get()
    future2.get()
    future3.get()
    future4.get()

    end_time = time.time()

    elapsed_time = end_time - start_time
    print('Elapsed Time: {0} s'.format(elapsed_time))

    pykka.ActorRegistry.stop_all()


if __name__ == '__main__':
    main()