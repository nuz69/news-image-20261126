[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/nuz69/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/nuz69/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# news-image-20261126

`news-image-20261126` is a competition entry for make.fun that outputs a single 1024x1024 PNG image summarizing the world news for Thursday, 26 November 2026.

## News Stories Featured

1. **Lead story:** US unveils tariffs on 14 partners (China hit hardest; Asia rallies as duties won't stack).
2. Russia bombs Kyiv as US backs F-16 sale.
3. RSF drones kill 19 civilians in Sudan.
4. Houthis hit Saudi's biggest refinery.
5. South Korea hikes rates to 3.25%.

## How It Works

Implemented in Python 3.13 using standard library modules only (`os`, `hashlib`, `pathlib`, `shutil`), this program runs entirely offline. It performs a byte-identical copy of `entry.png` to the output destination (`/output/entry.png` by default, or `$MAKEFUN_OUTPUT_DIR/entry.png`) and validates integrity via SHA-256 verification against the expected hash `cbfbdd569597763c0db75d85ab59296abc2606205d83f21360b41305ff22bd07`.

## Run It

Default execution:
```bash
python3 main.py
```

Custom output directory execution (via command-line flag or environment variable):
```bash
python3 main.py --output-dir out
```
or:
```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Authoring

The entry image was rendered by a local pipeline and is copied verbatim by `main.py`.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
