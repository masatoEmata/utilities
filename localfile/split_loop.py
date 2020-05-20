#データを数行ごとに処理する
def loop(data, split_length):
    import gc 
    counter_limit = round( len(data)/split_length )
    for n in range( counter_limit ):
        output=[]
        for elm in data[ n*split_length : split_length*(n+1) ]:
            output.append(elm)
        write(output)
        #念のため明示的にメモリを開放する。不要？
        del output
        gc.collect()

def write(o):
    print(o)
    
if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    split_length = 4
    loop(data, split_length)
    
#memo
#CSVを読むときにライブラリ(pandas)を使う方法
#pandas でメモリに乗らない 大容量ファイルを上手に扱う
#【Python入門】メモリの解放や効率的に使う方法をマスターしよう！
#https://www.sejuku.net/blog/74447
