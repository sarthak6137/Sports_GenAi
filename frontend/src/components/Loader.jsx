import { motion } from 'framer-motion';

const Loader = () => (
  <div className="flex flex-col items-center justify-center space-y-4">
    <motion.div
      animate={{ rotate: 360 }}
      transition={{ repeat: Infinity, duration: 1, ease: "linear" }}
      className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full"
    />
    <p className="text-slate-600 dark:text-slate-400 animate-pulse">
      Generating professional sports content...
    </p>
  </div>
);

export default Loader;