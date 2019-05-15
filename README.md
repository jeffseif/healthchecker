# healthchecker

Convenient frontend tooling for your home server

## Setup for basic usage

```bash
> git clone git@github.com:jeffseif/healthchecker.git
> cd healthchecker
> echo '{}' > config.json
> PORT=80 make &
> curl localhost
<html><tt>hello world ☃</tt></html>
> curl localhost/stats
<html><tt>    CPU: 3%<br>    Mem: 33%<br>    Disk: 17%<br>    Users: ['jeffseif']<br>    </tt></html>
```

## Advanced Usage

By adding a rule and directory path to `config.json`, `healthchecker` will automatically register a `Make` endpoint. When that endpoint is hit, `make -C [path]` will be run on your behalf.  The result is the ability to trigger latent apps on your server from a web browser on your phone!

```bash
> echo '{"/botw": ["/path/to/botw/git/", "all"]}' > config.json
> PORT=80 make &
> curl localhost/botw
<html><tt>make[1]: Entering directory '/path/to/botw/git/'<br>> Full Ancient armor<br>90: Ancient Gear<br>65: Ancient Spring<br>50: Ancient Shaft
...
```

## Keep a long-running daemon

`healthchecker` is designed so that (upon issuing `make`) only one daemon instance runs at a time.  This allows for convenient auto-recovery with `crontab`:

```bash
> crontab -l
# Once per hour, start healthchecker or restart it in case it has failed
0 * * * * PORT=80 make -C /path/to/healthchecker/git/
```
