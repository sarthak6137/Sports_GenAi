import { useState } from 'react';

const InputPanel = ({ onGenerate, loading }) => {
  const [formData, setFormData] = useState({
    sport: 'Cricket',
    content_type: 'Match Recap',
    match_title: '',
    highlights: '',
    tone: 'Professional',
    length: 'Medium'
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className="flex flex-col space-y-6">
      <h2 className="text-2xl font-bold text-blue-600 dark:text-blue-400">Content Studio</h2>
      
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-1">Sport</label>
          <select name="sport" onChange={handleChange} className="glass-input">
            <option>Cricket</option><option>Football</option><option>Basketball</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Match Title</label>
          <input 
            name="match_title" 
            placeholder="e.g. India vs Australia 2nd ODI" 
            onChange={handleChange} 
            className="glass-input" 
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Highlights</label>
          <textarea 
            name="highlights" 
            rows="4" 
            placeholder="Enter key moments..." 
            onChange={handleChange} 
            className="glass-input resize-none"
          />
        </div>

        <button 
          onClick={() => onGenerate(formData)}
          disabled={loading}
          className="w-full py-3 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-bold rounded-xl transition-all transform hover:scale-[1.02] active:scale-95 disabled:opacity-50"
        >
          {loading ? 'Processing...' : 'Generate Content'}
        </button>
      </div>
    </div>
  );
};

export default InputPanel;