import json
from src.process.process import Process


def main():
    # Read config
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    process = Process()
    process.app_run(config)


if __name__ == '__main__':
    main()