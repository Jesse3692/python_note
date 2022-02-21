# powershell使用

## 常用命令

查看历史命令记录

```shell
Get-Content (Get-PSReadlineOption).HistorySavePath
```

## 脚本命令

获取git默认分支

```powershell
$a = git branch
$a.Substring(2)
```

获取日期

```powershell
$b = Get-Date -Format 'yyyy.M.d'
```

休眠一秒

```powershell
Start-Sleep -s 1
```

记录路径

```powershell
$c = pwd
$c = $c.Path
```

与终端进行交互

```powershell
Read-Host 'Commit Info?'
```

