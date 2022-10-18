import Note from "./components/Note";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Note title="Receita de miojo">
        Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque
        em uma vasilha e aproveite seu snack :)
      </Note>
      <Note title="Sorvete de banana">
        Coloque a banana no congelador e espere.
      </Note>
    </div>
  );
}

export default App;