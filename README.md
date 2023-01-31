This repository showcases a potential bug :-)


An operation that supports two methods "EASOM" and "ABSMIN" requires different parameters for each method. 
This could be, for example, different hyper-parameters for two different optimizers.

```
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=None)
    parser.add_argument("--y", type=float, default=None)
    parser.add_argument("--a", type=float, default=None)
    parser.add_argument("--b", type=float, default=None)
    parser.add_argument(
        "--method",
        type=str,
        choices=["EASOM", "ABSMIN"],
    )
    # --------------------
    args = parser.parse_args()
```



First we create some runs for the first method
```
guild run -y op_optimize method=ABSMIN a=1 b=1
```

then some random runs for the second method:
```guild run -y op_optimize method="EASOM" x="[0.:2.]" y="[0.:2.]"  --optimizer=random --minimize loss --max-trials 5  -t optimize_runs```

In the `guild.yml` we set the `prev-trials` to use previous runs of this operation:
```
  optimizer:
    algorithm: gp
    prev-trials: operation
```
However, this fails:
```guild run -y op_optimize method="EASOM" x="[0.:2.]" y="[0.:2.]"  --optimizer=gp  --minimize loss --max-trials 5  -t optimize_runs```

If we clean up, and retry without the first method:
```
guild runs delete -y -Fo op_optimize
guild run -y op_optimize method="EASOM" x="[0.:2.]" y="[0.:2.]"  --optimizer=random --minimize loss --max-trials 5  -t optimize_runs
guild run -y op_optimize method="EASOM" x="[0.:2.]" y="[0.:2.]"  --optimizer=gp  --minimize loss --max-trials 5  -t optimize_runs
```

it works.
