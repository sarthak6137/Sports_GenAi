import ThemeToggle from './ThemeToggle';
import { Trophy } from 'lucide-react';

const Header = () => {
  return (
    <header className="sticky top-0 z-50 w-full backdrop-blur-md bg-white/70 dark:bg-slate-900/70 border-b border-slate-200 dark:border-slate-800 transition-colors duration-500">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Logo and Title */}
        <div className="flex items-center gap-2">
          <div className="p-2 bg-blue-600 dark:bg-blue-500 rounded-lg text-white">
            <Trophy size={24} />
          </div>
          <h1 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400">
            SportsGenAI Studio
          </h1>
        </div>

        {/* Right Side Controls */}
        <div className="flex items-center gap-4">
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
};

export default Header;