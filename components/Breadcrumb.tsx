import Link from 'next/link';

interface BreadcrumbItem {
  label: string;
  href?: string;
  current?: boolean;
}

interface BreadcrumbProps {
  items: BreadcrumbItem[];
}

export default function Breadcrumb({ items }: BreadcrumbProps) {
  return (
    <nav aria-label="Breadcrumb" className="mb-6">
      <div className="bg-gradient-to-r from-amber-900/20 to-amber-800/20 border border-amber-700/30 rounded-lg px-4 py-2">
        <ol className="flex items-center space-x-2 text-sm">
          {items.map((item, index) => (
            <li key={index} className="flex items-center">
              {index > 0 && (
                <span className="text-amber-500/60 mx-2" aria-hidden="true">
                  →
                </span>
              )}
              
              {item.current ? (
                <span className="text-amber-200 font-medium">
                  {item.label}
                </span>
              ) : item.href ? (
                <Link
                  href={item.href}
                  className="text-amber-300 hover:text-amber-100 transition-colors font-medium"
                >
                  {item.label}
                </Link>
              ) : (
                <span className="text-amber-400">
                  {item.label}
                </span>
              )}
            </li>
          ))}
        </ol>
      </div>
    </nav>
  );
}