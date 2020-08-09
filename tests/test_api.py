import requests


def test_all_breed_list():
    """
    Test all breeds list api
    """
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    # Status code
    assert response.status_code == 200
    # Header
    assert response.headers['Content-Type'] == "application/json"


def test_sub_breed():
    """
    Test sub breed list api
    """
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    # Body sub breed
    response_body = response.json()
    assert response_body["message"] == ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]


def test_akita_image():
    """
    Test sub breed list api
    """
    response = requests.get("https://dog.ceo/api/breed/akita/images")
    response_body = response.json()
    expected = [
            "https://images.dog.ceo/breeds/akita/512px-Ainu-Dog.jpg",
            "https://images.dog.ceo/breeds/akita/512px-Akita_inu.jpeg",
            "https://images.dog.ceo/breeds/akita/Akina_Inu_in_Riga_1.jpg",
            "https://images.dog.ceo/breeds/akita/Akita_Dog.jpg",
            "https://images.dog.ceo/breeds/akita/Akita_Inu_dog.jpg",
            "https://images.dog.ceo/breeds/akita/Akita_hiking_in_Shpella_e_Pellumbasit.jpg",
            "https://images.dog.ceo/breeds/akita/Akita_inu_blanc.jpg",
            "https://images.dog.ceo/breeds/akita/An_Akita_Inu_resting.jpg",
            "https://images.dog.ceo/breeds/akita/Japaneseakita.jpg"
        ]
    # Body breed images
    assert response_body["message"] == expected
