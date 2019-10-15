"""Ascending"""
def main():
    """code"""
    liss = []
    for _ in range(5):
        num = int(input())
        liss.append(num)
    liss.sort()
    for i in liss:
        print(i)
main()
