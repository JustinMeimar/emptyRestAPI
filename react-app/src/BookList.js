import React, { Component } from 'react';
import BookManage from './BookManage';

const BookList = new BookManage();

class BookList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            books: [],
            nextPageURL: ''
        };

        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this)
    }

    componentDidMount() {
        var self = this;
        BookManage.getBooks().then(function (result) {
            self.setState({books:result.data, nextPageURL: result.nextlink})

        });
    }

    render() {
        return(
            <div className="books--list">
                <table className="table">
                    <thead key="thead">
                    <tr>
                        <th>#</th>
                        <th>Book Title</th>
                        <th>Author First</th>
                        <th>Author Last</th>
                        <th>Date Published</th>
                        <th>Genre</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.books.map(c =>
                    <tr key={c.pk}>
                        <td>{c.book-title}</td>
                        <td>{c.author_first}</td>
                        <td>{c.author_last}</td>
                        <td>{c.date_published}</td>
                        <td>{c.genre}</td>
                    
                    </tr>                    
                    )}
                    </tbody>
                </table>
            </div>
        )

    }

}

export default BookList;