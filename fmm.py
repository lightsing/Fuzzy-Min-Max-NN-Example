#!/usr/bin/env python3

import configparser

def get_config(path):
    config = configparser.ConfigParser()
    config.optionxform=str
    try:
        config.read(path)
        return config
    except Exception as e:
        print(e)

def main():
    pass

if __name__ == '__main__':
    main()
