def adjust_col(ws):
    for col in ws.columns:
        max_length = 0
        column = col[0].column # Get the column name
        column = chr(ord("A") - 1 + column)
        for cell in col:
            try: # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                 pass
        adjusted_width = (max_length + 2) * 1.1
        print(adjusted_width)
        ws.column_dimensions[column].width = adjusted_width
    # https://stackoverflow.com/questions/39529662/python-automatically-adjust-width-of-an-excel-files-columns
    # これのサンプルコードが動かないので直したもの
    
def main(file_name):
    import openpyxl as xl
    inputfile = file_name

    # read input sheet - just 1 column
    wb = xl.load_workbook(filename=inputfile)
    
    i = 0
    while i < len(wb.worksheets):
        ws = wb.worksheets[i]
        adjust_col(ws)
        i += 1
        
    # save xlsx file
    wb.save(inputfile)
    
if __name__ == "__main__":
    main('output.xlsx')