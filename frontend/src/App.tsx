import { HashRouter, Routes, Route } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Landing } from './pages/Landing';
import { Dashboard } from './pages/Dashboard';
import { Course } from './pages/Course';
import { Lesson } from './pages/Lesson';
import './index.css';

function App() {
  return (
    <HashRouter>
      <Routes>
        {/* Lesson Page - Fullscreen, no Layout wrapper */}
        <Route path="lesson/:id" element={<Lesson />} />

        {/* Pages with Layout wrapper */}
        <Route path="/" element={<Layout />}>
          <Route index element={<Landing />} />
          <Route path="catalog" element={<Dashboard />} />
          <Route path="course/:slug" element={<Course />} />
        </Route>
      </Routes>
    </HashRouter>
  );
}


export default App;
