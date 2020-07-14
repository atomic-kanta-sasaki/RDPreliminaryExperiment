# RDPreliminaryExperiment
大学研究用プログラムファイル
#### 現状
pythonでどんぐらいのことができるのか調べている
ほとんど殴り書きコードのためメモがわりに使用
dockerを使用するとPCがLinuxだと判定されてしまい, 使用したいライブラリが使用できないため今回は一旦dockerを使用しない方向で実装する

#### chorme driverが入らないときに参考にすること
 - https://qiita.com/hanzawak/items/2ab4d2a333d6be6ac760

#### chromeを起動する方法
 - "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9222 --user-data-dir=C:\Temp_ForChrome
 このコマンドを使用しChromeを起動する <br />
 このコマンドを使用することですでに開いているChromeに対してSeleniumを使用して操作を行うことができる.<br />
 これを使用しないとChromeDriverを起動するたびに新しいブラウザを開いてしまうため非常に厄介なことになる.

dockerコンテナに入る
```
docker exec -i -t CONTAINER_ID /bin/bash
```
