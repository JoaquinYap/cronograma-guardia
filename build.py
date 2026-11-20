# Une src/app.html + src/exceljs.min.js en un solo archivo: cronograma.html
import pathlib
b = pathlib.Path(__file__).parent
html = (b/'src'/'app.html').read_text(encoding='utf-8')
js = (b/'src'/'exceljs.min.js').read_text(encoding='utf-8').replace('</script', '<\\/script')
out = html.replace('<!--EXCELJS-->', '<script>\n' + js + '\n</script>')
(b/'cronograma.html').write_text(out, encoding='utf-8')
print('OK', len(out)//1024, 'KB')
