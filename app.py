
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Используем SQLite как базу данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель базы данных
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

# Глобальный маршрут для отображения всех элементов
@app.route('/')
def index():
    items = Item.query.all()  # Получаем все элементы из базы данных
    return render_template('index.html', items=items)

# Маршрут для добавления нового элемента
@app.route('/add', methods=['POST'])
def add():
    item_name = request.form['item_name']
    new_item = Item(name=item_name)  # Создаем новый элемент
    db.session.add(new_item)  # Добавляем элемент в сессию
    db.session.commit()  # Сохраняем изменения
    return 'Item added!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных
    app.run(host='0.0.0.0', port=5000) # Запускаем приложение
