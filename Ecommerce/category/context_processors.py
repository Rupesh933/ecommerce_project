# from .models import Category

# # context processor to make the category available in all templates without explicitly passing it in the context of each view
# def menu_links(request):
#     links = Category.objects.all()
#     return dict(links=links) # links is the name of the variable that will be available in the templates, and it contains all the category objects from the database

# # not working ----20----

# category/context_processors.py
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    
    # This prints directly to your terminal logs when you refresh the page
    print("\n=== DEBUGGING CATEGORIES ===")
    print(f"Total categories found in DB: {links.count()}")
    for c in links:
        print(f" -> Category object string: {c}")
    print("=============================\n")
    
    return dict(links=links)