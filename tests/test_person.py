import pytest
from viewing_party.person import Person

def test_add_movie():
    # Arrange
    name1 = "Kendall"
    watched1 = ["Movie1", "Movie2", "Movie3"]
    friends1 = ["Jasmine"]
    subscriptions1 = ["Netflix", "Hulu"]
    person1 = Person(name1, watched1, friends1, subscriptions1)
    movie4 = "Movie4"
    
    # Act
    person1.add_watched(movie4)

    # Assert
    assert len(person1.watched) == 4
    assert person1.watched == ["Movie1", "Movie2", "Movie3", "Movie4"]