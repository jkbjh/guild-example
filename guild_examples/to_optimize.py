import argparse
import numpy as np


def easom(x, y):
    return np.cos(x) * np.cos(y) * np.exp(-((x-np.pi)**2 + (y - np.pi)**2))


def absmin(a, b):
    return np.abs(a - 2) + np.abs(b - 1.5)


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
    eps = np.random.normal()
    if args.method == "EASOM":
        value = easom(args.x, args.y) + eps
    elif args.method == "ABSMIN":
        value = absmin(args.a, args.b) + eps
    else:
        raise RuntimeError("method not selected")
    print(f"loss: {value}")

if __name__ == "__main__":
    main()
