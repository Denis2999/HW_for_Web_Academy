def count_words(lorem):
    from collections import Counter
    lorem = lorem.replace(",", "")
    lorem = lorem.replace(".", "")
    words = lorem.split()

    return Counter(words)


print(count_words("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " 
                  "Pellentesque bibendum tristique nisl quis facilisis. " 
                  "Nunc auctor dolor et arcu tempor, Calvin Klein Calvin Klein" 
                  " Calvin Klein et dignissim urna molestie." 
                  " Suspendisse pellentesque metus non dui consequat ultrices."
                  " Vestibulum auctor dui vel purus rhoncus, Calvin Klein "
                  "Calvin Klein Calvin Klein quis fermentum nibh dictum. "
                  "Vestibulum viverra a ligula quis iaculis." 
                  " Praesent turpis diam, mattis in risus eget, pretium ornare sapien. " 
                  "Sed eu augue quis orci elementum euismod."))
