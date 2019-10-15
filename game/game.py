import sys
import argparse
from webview import WebView
from controller import Controller


def main():
    """
    Main function to follow python standards to initiate the game.
    Takes one argument, a flag to start a webserver with webview
    :return:
    """
    argparser = argparse.ArgumentParser(description='choose web view')
    argparser.add_argument('-w', action='store_true',
                           default=False, help='choose to use webview')

    # Parse the argument
    args = argparser.parse_args()

    # vars returns a dict from args
    if vars(args)['w'] is True:
        cntrlr = WebView()
    else:
        cntrlr = Controller()
        cntrlr.main_menu()

if __name__ == "__main__":
    main()
