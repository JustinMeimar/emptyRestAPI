import axios from 'axios';
const API_URl = 'http://localhost:3000';

export default class BookManage {

    constructor(){}

    getBooks() {
        console.log("get books");
        const url = `${API_URL}/api/books`;
        return axios.get(url).then(response => response.data);
    }
}