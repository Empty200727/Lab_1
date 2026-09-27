import pytest

import main


def test_distance_table_is_symmetric(task):
    module = task('00_distance')
    table = module.build_distance_table({'O': (0, 0), 'P': (6, 8), 'Q': (0, 8)})

    assert table['O']['P'] == pytest.approx(10)
    assert table['P']['O'] == table['O']['P']
    assert table['P']['Q'] == pytest.approx(6)
    assert 'O' not in table['O']


def test_distance_table_for_given_cities(task):
    module = task('00_distance')
    table = module.build_distance_table(module.sites)

    assert table['London']['Paris'] == pytest.approx(42.4264, abs=1e-4)


def test_circle_area(task):
    assert task('01_circle').circle_area(42) == pytest.approx(5541.7693464)


@pytest.mark.parametrize('point, expected', [
    ((23, 34), True),
    ((30, 30), False),
    ((0, 42), True),
    ((-42, 1), False),
])
def test_point_in_circle(task, point, expected):
    assert task('01_circle').point_in_circle(point, 42) is expected


def test_expressions(task):
    module = task('02_operations')

    assert module.sample_expression() == 9
    assert module.target_expression() == 25


def test_movies_slices(task):
    module = task('03_favorite_movies')
    picked = module.pick_movies(module.my_favorite_movies)

    assert list(picked.values()) == ['Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие']
    assert all(',' not in title for title in picked.values())


def test_family(task):
    module = task('04_my_family')

    assert module.height_of(module.my_family_height, 'Отец') == 178
    assert module.total_height(module.my_family_height) == 860
    with pytest.raises(KeyError):
        module.height_of(module.my_family_height, 'Дядя')


def test_zoo_steps(task):
    module = task('05_zoo')
    steps = module.zoo_steps(module.zoo, module.birds)

    assert steps[0][:3] == ['lion', 'bear', 'kangaroo']
    assert steps[1][-3:] == module.birds
    assert 'elephant' not in steps[2]
    assert module.zoo == ['lion', 'kangaroo', 'elephant', 'monkey']


@pytest.mark.parametrize('animal, cage', [('lion', 1), ('lark', 7)])
def test_cage_numbers(task, animal, cage):
    module = task('05_zoo')
    final = module.zoo_steps(module.zoo, module.birds)[-1]

    assert module.cage_of(final, animal) == cage


def test_songs(task):
    module = task('06_songs_list')

    assert module.duration_from_list(module.violator_songs_list, module.LIST_TITLES) == 14.93
    assert module.duration_from_dict(module.violator_songs_dict, module.DICT_TITLES) == 13.49


def test_secret(task):
    module = task('07_secret')

    assert module.decode(module.secret_message) == 'в бане веник дороже денег'


def test_garden(task):
    module = task('08_garden')
    garden, meadow = module.garden_set, module.meadow_set

    assert module.common_flowers(garden, meadow) == {'ромашка', 'одуванчик'}
    assert module.only_in(garden, meadow) == {'роза', 'гладиолус', 'подсолнух'}
    assert module.only_in(meadow, garden) == {'клевер', 'мак'}
    assert len(module.all_flowers(garden, meadow)) == 7


def test_sweets_match_automatic_choice(task):
    module = task('09_shopping')

    assert module.sweets == module.cheapest_offers(module.shops)


@pytest.mark.parametrize('name, expected', [
    ('Лампа', (27, 1134)),
    ('Стол', (54, 27860)),
    ('Диван', (3, 3550)),
    ('Стул', (105, 10311)),
])
def test_stock_report(task, name, expected):
    module = task('10_store')

    assert module.stock_report(module.goods, module.store)[name] == expected


def test_main_finds_all_tasks():
    tasks = main.discover_tasks()

    assert len(tasks) == 11
    assert tasks[0] == '00_distance' and tasks[-1] == '10_store'


def test_main_runs_selected_task(capsys):
    main.main(['7'])

    output = capsys.readouterr().out
    assert '07_secret' in output
    assert 'в бане веник дороже денег' in output
