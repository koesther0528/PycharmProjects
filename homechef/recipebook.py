from recipe import Recipe

class RecipeBook:
    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

    def add_recipe(self):
        # 추가할 레시피 이름 입력받기
        name = input('>> 레시피 이름을 입력하세요: ')
        # 중복 체크 확인하기
        for recipe in self.recipe_list:
            if name == recipe.name:
        # 중복 O -> 중복 알려주기
                print('이미 존재하는 레시피입니다.')
                return
       # 중복 X -> 레시피 생성 -> 레시피 리스트에 추가하기
        new_recipe = Recipe(name)
        new_recipe.set_recipe()
        self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1}')
            print(recipe)

    def search_recipe(self):
        searched_recipe = []
        # 레시피 이름 입력받기
        name = input('>> 원하는 레시피를 검색하세요: ')
        # 레시피 리스트 이름 확인하기
        for recipe in self.recipe_list:
            if name == recipe.name:
        # 레시피 이름 출력하기
                print(recipe)
                searched_recipe.append(recipe)
        # 검색된 레시피 없다면 추가하기
        if len(searched_recipe) == 0:
            answer = input('>> 찾는 레시피가 없습니다. 추가하시겠습니까?(1: 예, 0: 아니오)')
            if answer == '1':
                self.add_recipe()
            else:
                return

    # 재료로 레시피 찾기
    def search_ingredient(self):
        # 빈 셋 생성하기
        all_ingredient = set()
        # 레시피북의 레시피재료 set에 넣기
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredient:
                all_ingredient.add(ingredient)
        # 모든 재료 보여주기
        for index, ingredient in enumerate(all_ingredient):
            print(f'{index + 1}. {ingredient}')
        # 찾을 재료 입력하기
        search_num = int(input('>> 사용할 재료를 입력하세요: '))
        search_ingredient = list(all_ingredient)[search_num-1]
        # 레시피 재료 살펴보기
        for recipe in self.recipe_list:
            # 입력한 재료가 포함된 레시피 보여주기
            if search_ingredient in recipe.ingredient:
                print(recipe)

    def init_recipe(self):
        떡볶이 = Recipe('떡볶이')
        떡볶이.people = 2
        떡볶이.video = "youtube.com"
        떡볶이.ingredient = {'떡':'200', '고추장':'100', '어묵':'200', '양파':'300', '물':'100'}
        self.recipe_list.append(떡볶이)
        카레 = Recipe('카레')
        카레.ingredient = {'카레가루':'200', '감자':'200', '당근':'200'}
        self.recipe_list.append(카레)
        파스타 = Recipe('파스타')
        파스타.ingredient = {'파스타 면':'200', '파스타 소스':'200'}
        파스타.contents = '맛있게드세요!'
        self.recipe_list.append(파스타)