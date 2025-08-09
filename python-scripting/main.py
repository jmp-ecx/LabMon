import script_engine as se

def main() -> None:
    script = se.Script('./scripts/test.py').load()
    ctx    = se.Context()

    se.run_threaded(script, ctx)

if __name__ == "__main__":
    main()
