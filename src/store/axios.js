import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:5000'

const getCharacter = () => { return 1 }

const getQuests = async hero_id => {
  try {
    const response = await axios.get(`${BASE_URL}/quests?hero_id=${hero_id}`)

    return response.data
  } catch (err) {
    console.error(err)
  }
}

export default {
  getCharacter,
  getQuests
}