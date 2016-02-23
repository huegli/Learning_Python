from nose.tools import *
from ex48 import parser

def test_Sentence():
    a_sentence = parser.Sentence(('noun', 'Player'),
                                 ('verb', 'kill'),
                                 ('noun', 'Monster'))
    assert_equal(a_sentence.subject, "Player")
    assert_equal(a_sentence.verb, "kill")
    assert_equal(a_sentence.obj, "Monster")

def test_peek():
    assert_equal(parser.peek([]), None)
    assert_equal(parser.peek([('noun', 'Boss')]), 'noun')

def test_match():
    assert_equal(parser.match([],''), None)
    assert_equal(parser.match([('noun', 'Boss')], 'something'), None)
    assert_equal(parser.match([('noun', 'Boss')], 'noun'), ('noun', 'Boss'))
    assert_equal(parser.match([('noun', 'Boss'),
                               ('verb', 'kill')], 'noun'), ('noun', 'Boss'))

def test_skip():
    assert_equal(parser.skip([],''), None)
    word_list = [('stop', 'the'),
                 ('stop', 'slow'),
                 ('verb', 'kill')]
    parser.skip(word_list, 'stop')
    assert_equal(word_list, [('verb', 'kill')])

def test_parse_verb():
    word_list = [('stop', 'the'),
                 ('stop', 'slow'),
                 ('verb', 'kill')]
    assert_equal(parser.parse_verb(word_list), ('verb', 'kill'))
    assert_equal(word_list, [])
    error_list = [('stop', 'the'),
                  ('noun', 'cow')]
    assert_raises(parser.ParserError, parser.parse_verb, error_list)

def test_parse_object():
    word_list = [('stop', 'the'),
                 ('noun', 'cow')]
    assert_equal(parser.parse_object(word_list), ('noun', 'cow'))
    assert_equal(word_list, [])
    dir_list = [('stop', 'way'),
                ('direction', 'up')]
    parser.parse_object(dir_list)
    assert_equal(dir_list, [])
    error_list = [('stop', 'way'),
                  ('verb', 'run')]
    assert_raises(parser.ParserError, parser.parse_object, error_list)


def test_parse_subject():
    word_list = [('stop', 'the'),
                 ('noun', 'cow')]
    assert_equal(parser.parse_subject(word_list), ('noun', 'cow'))
    assert_equal(word_list, [])
    verb_list = [('stop', 'way'),
                 ('verb', 'run')]
    assert_equal(parser.parse_subject(verb_list), ('noun', 'player'))
    error_list = [('stop', 'way'),
                  ('direction', 'down')]
    assert_raises(parser.ParserError, parser.parse_subject, error_list)

def test_parse_sentence():
    a_sentence = parser.parse_sentence(
            [('noun', 'Wizard'),
             ('verb', 'kill'),
             ('noun', 'Troll')])
    assert_equal(a_sentence.subject, 'Wizard')
    assert_equal(a_sentence.verb, 'kill')
    assert_equal(a_sentence.obj, 'Troll')
