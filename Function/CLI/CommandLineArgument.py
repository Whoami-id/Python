import sys



def main():
    print(len(sys.argv))
    print(sys.argv)

    for arg in sys.argv[1:]:
        print(arg, type(arg))



if __name__ == "__main__":
    main()