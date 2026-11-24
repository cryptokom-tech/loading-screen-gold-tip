# Loading Screen Gold: A Tip in 200 Characters

[![make.fun](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/cryptokom-tech/loading-screen-gold-tip/rank.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/cryptokom-tech/loading-screen-gold-tip/reward.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for the [Loading Screen Gold: A Tip in 200 Characters](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) bounty on [make.fun](https://make.fun).

## The entry

One sharp, funny loading-screen tip for stressed developers and AI coding
agents, 200 characters or fewer:

> Tip: if this screen outlasts your patience, blame the prompt, not the agent — it only did exactly what you said.

## How it works

`main.py` (Python 3, standard library only) writes that single line to
`/output/entry.txt`. The output is fully deterministic: no network, no
randomness, nothing read from outside this repository. The program exits
non-zero if the line is empty, multi-line, or over 200 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
