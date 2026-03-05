import { useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import InputPanel from '../components/InputPanel';
import Loader from '../components/Loader';
import { motion } from 'framer-motion';

const Dashboard = () => {
  const [article, setArticle] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async (formData) => {
    setLoading(true);
    try {
    const response = await axios.post('http://localhost:8000/generate-content', formData);
    // The backend now returns { "article": "..." }, so we use:
    setArticle(response.data.article);
    } catch (error) {
      console.error("Error connecting to backend:", error);
      alert("Make sure your Python backend is running on port 8000!");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1 max-w-7xl mx-auto w-full px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          <div className="glass-card p-8">
            <InputPanel onGenerate={handleGenerate} loading={loading} />
          </div>

          <div className="glass-card p-8 overflow-y-auto max-h-[80vh]">
            {loading ? <Loader /> : (
              article ? (
                <div className="prose dark:prose-invert max-w-none">
                  <div className="whitespace-pre-wrap text-slate-700 dark:text-slate-300">
                    {article}
                  </div>
                </div>
              ) : (
                <div className="h-full flex flex-col items-center justify-center text-slate-400">
                  <p>Your AI-generated article will appear here.</p>
                </div>
              )
            )}
          </div>

        </div>
      </main>
    </div>
  );
};

export default Dashboard;