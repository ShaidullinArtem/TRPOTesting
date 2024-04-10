from test.algoritmika import AlgoritmikaTest
from test.dribbble.test import DribbbleTest
from test.vk import VKTest


def main() -> None:

    # TODO  Algoritmika tests
    # algoritmika = AlgoritmikaTests('http://algoritmika.org/ru')
    # print(algoritmika.header_test('header__logo'))
    # print(algoritmika.is_visible_test('start-section__btn'))
    # algoritmika.nav_to_link_test('https://motka.design/')
    # algoritmika.enter_input_test('sub-email', 'test@gmail.com')
    # algoritmika.click_test('partner-footer__mailing-btn')

    # TODO Dribbble tests
    # dribble = DribbbleTest('https://dribbble.com/')
    # print(dribble.header_test('hero__heading'))
    # print(dribble.is_visible_test('home-feed__heading home-container'))
    # dribble.nav_to_link_test('https://dribbble.com/signup/new')
    # dribble.enter_input_test('nav-v2-search__input', 'moblie app')
    # dribble.click_test('nav-v2-logo')

    # TODO VK tests
    # vk = VKTest('https://vk.com/')
    # print(vk.header_test('VkIdForm__header'))
    # print(vk.is_visible_test('footer_copy'))
    # vk.nav_to_link_test('https://vk.com/about')
    # vk.enter_input_test('index_email', '+79999999999')
    # vk.click_test('FlatButton__in')
    return


if __name__ == '__main__':
    main()
