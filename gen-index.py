import sys
import time

HTML_STR = '''
<meta http-equiv="pragma" content="no-cache" />
<html>
  <head>
    <title>Sangho Lee</title>
    <script src="//static.getclicky.com/js" type="text/javascript"></script>
    <script type="text/javascript">try{ clicky.init(100925728); }catch(e){}</script>
    <script src='jquery.js'></script>
    <script src='legacy.js'></script>
    <script src='flatdoc.js?%s'></script>

    <script>
      Flatdoc.run({
        fetcher: Flatdoc.file('sangho.md?%s')
      });
    </script>
    <style>
      body { font-family: arial; }
      h1 { color: midnightblue; }
      h2 { color: midnightblue; }
      h3 { color: midnightblue; }
      ul, ol { list-style: none; margin-left: 1em; padding: 0px; }
    </style>
  </head>

  <body role='flatdoc'>
    <div role='flatdoc-content'></div>
  </body>
</html>
'''

def main():
    idx_file = ''
    if len(sys.argv) == 2:
        idx_file = sys.argv[1]
    else:
        idx_file = 'index.html'

    f = open(idx_file, 'w')
    f.write(HTML_STR % (str(time.time()), str(time.time())))
    f.close()

if __name__ == '__main__':
    main()
