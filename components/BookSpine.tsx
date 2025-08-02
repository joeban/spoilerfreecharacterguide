'use client';

interface BookSpineProps {
  title: string;
  author: string;
  bookCount: number;
}

export default function BookSpine({ title, author, bookCount }: BookSpineProps) {
  // Generate consistent colors based on the series
  const colorIndex = title.length % 6;
  const bookColors = [
    { primary: '#7f1d1d', secondary: '#991b1b', accent: '#dc2626' }, // red
    { primary: '#1e3a8a', secondary: '#2563eb', accent: '#3b82f6' }, // blue
    { primary: '#14532d', secondary: '#166534', accent: '#22c55e' }, // green
    { primary: '#581c87', secondary: '#7c3aed', accent: '#a855f7' }, // purple
    { primary: '#a16207', secondary: '#ca8a04', accent: '#eab308' }, // yellow
    { primary: '#312e81', secondary: '#4f46e5', accent: '#6366f1' }, // indigo
  ];
  
  const colors = bookColors[colorIndex];
  
  return (
    <div className="book-cover group relative transition-all duration-500 hover:scale-105 hover:-translate-y-2"
         style={{ perspective: '1000px' }}>
      <div className="relative"
           style={{ transformStyle: 'preserve-3d' }}>
        
        {/* Book spine (left side) */}
        <div className="absolute left-0 top-0 bottom-0 w-8 md:w-12"
             style={{
               backgroundColor: colors.secondary,
               transform: 'rotateY(-90deg) translateZ(16px)',
               transformOrigin: 'left',
               boxShadow: 'inset 2px 0 4px rgba(0,0,0,0.3)',
             }}>
          {/* Spine decoration */}
          <div className="h-full flex items-center justify-center">
            <div className="w-px h-3/4 bg-gradient-to-b from-transparent via-gold to-transparent opacity-50" />
          </div>
        </div>
        
        {/* Book cover (front) */}
        <div className="relative w-48 md:w-56 h-72 md:h-80 rounded-r-sm overflow-hidden"
             style={{
               backgroundColor: colors.primary,
               boxShadow: '0 10px 30px rgba(0,0,0,0.3), inset -2px 0 4px rgba(0,0,0,0.2)',
               transform: 'translateZ(0)',
             }}>
          
          {/* Cover texture/pattern */}
          <div className="absolute inset-0 opacity-10"
               style={{
                 backgroundImage: `repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,0.1) 10px, rgba(255,255,255,0.1) 20px)`
               }} />
          
          {/* Gold border frame */}
          <div className="absolute inset-4 border-2 border-gold opacity-60 rounded-sm" />
          
          {/* Title and author */}
          <div className="absolute inset-0 flex flex-col items-center justify-center p-8 text-center">
            {/* Series title */}
            <h3 className="text-xl md:text-2xl font-display font-bold mb-4 text-parchment"
                style={{ 
                  textShadow: '2px 2px 4px rgba(0,0,0,0.5)',
                  letterSpacing: '0.05em'
                }}>
              {title}
            </h3>
            
            {/* Decorative divider */}
            <div className="w-24 h-px bg-gradient-to-r from-transparent via-gold to-transparent mb-4" />
            
            {/* Author */}
            <p className="text-sm md:text-base text-parchment-dark"
               style={{ 
                 textShadow: '1px 1px 2px rgba(0,0,0,0.5)',
                 letterSpacing: '0.1em'
               }}>
              {author}
            </p>
            
            {/* Book count badge */}
            {bookCount > 1 && (
              <div className="absolute bottom-6 right-6">
                <div className="bg-gold text-ink text-sm font-bold rounded-full w-10 h-10 flex items-center justify-center shadow-lg">
                  {bookCount}
                </div>
              </div>
            )}
          </div>
          
          {/* Cover highlight/shine effect */}
          <div className="absolute inset-0 bg-gradient-to-br from-white/10 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
        </div>
        
        {/* Book top (pages edge) */}
        <div className="absolute top-0 left-8 md:left-12 right-0 h-4"
             style={{
               backgroundColor: '#f4e8d0',
               transform: 'rotateX(90deg) translateZ(8px)',
               transformOrigin: 'top',
               boxShadow: 'inset 0 2px 3px rgba(0,0,0,0.1)',
             }}>
          {/* Page lines */}
          <div className="h-full w-full"
               style={{
                 backgroundImage: 'repeating-linear-gradient(90deg, rgba(139,69,19,0.1) 0px, rgba(139,69,19,0.1) 1px, transparent 1px, transparent 3px)'
               }} />
        </div>
        
        {/* Shadow for 3D effect */}
        <div className="absolute -bottom-2 left-2 right-2 h-2 bg-black/20 rounded-full blur-md transform group-hover:scale-110 transition-transform duration-500" />
      </div>
    </div>
  );
}
