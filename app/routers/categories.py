from fastapi import APIRouter

router = APIRouter(
    prefix='/categories',
    tags=['categories'],
)


@router.get('/')
async def get_all_categories():
    """
    Возвращает список всех категорий товаров
    """
    return {'message': 'List of all categories'}


@router.post('/')
async def create_category():
    """
    Создает новую категорию товаров
    """
    return {'message': 'Category created'}


@router.put('/{category_id}')
async def update_category(category_id: int):
    """
    Удаляет категорию по ее ID
    """
    return {'message': f'Category with id {category_id} updated'}


@router.delete('/{category_id}')
async def delete_category(category_id: int):
    """
    Удаляет категорию по ее ID
    """
    return {'message': f'Category with id {category_id} deleted'}
