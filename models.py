def conectar_db(data_base) :
    class Usuario(data_base.Model):
    
        id = data_base.Column(data_base.Integer, primary_key=True)
        nombre = data_base.Column(data_base.String(50), nullable=False)
        email = data_base.Column(data_base.String(120), unique=True, nullable=False)

        def __repr__(self):
            return f'<Usuario {self.nombre}>'
    