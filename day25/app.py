def run():
    fileName = "day25/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    decimal_sum = sum([to_dec(line) for line in lines])
    snafu_sum = to_snafu(decimal_sum)
    print(f"DECIMAL: {decimal_sum}")
    print(f"SNAFU: {snafu_sum}")
    assert decimal_sum == to_dec(snafu_sum)

def to_dec(snafu):
    sum = 0
    for i,n in enumerate(reversed(snafu)):
        dec_val = ("=-012".rindex(n)-2) * (5**i)
        sum += dec_val
    return sum

def to_snafu(decimal):
    snafu = ""
    while decimal != 0:
        decimal, remainder = divmod(decimal + 2, 5) # decimal = (d+2) // 5, remainder = (d+2) % 5
        x = "=-012"[remainder]
        snafu += str(x)
    return snafu[::-1]

assert to_snafu(4890) == "2=-1=0" and to_dec("2=-1=0") == 4890
run()
