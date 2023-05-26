print(
    len(
        {
            i.replace('b','d',1) if i.startswith('b') else i.replace('c','')
            for i in ['aa','bbb','cccc', 'bacbac'] if len(i) > 2
        }
    )
)