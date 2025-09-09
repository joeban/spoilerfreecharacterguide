import { ImageResponse } from 'next/og'

export const runtime = 'edge'

export const size = {
  width: 180,
  height: 180,
}

export const contentType = 'image/png'

export default function AppleIcon() {
  return new ImageResponse(
    (
      <div
        style={{
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: '#1a1108',
          borderRadius: 36,
        }}
      >
        <div
          style={{
            display: 'flex',
            width: 120,
            height: 140,
            position: 'relative',
          }}
        >
          {/* Book spine */}
          <div
            style={{
              width: 20,
              height: 140,
              backgroundColor: '#8B4513',
              borderTopLeftRadius: 4,
              borderBottomLeftRadius: 4,
              boxShadow: 'inset 2px 0 4px rgba(0,0,0,0.3)',
            }}
          />
          {/* Book cover */}
          <div
            style={{
              width: 100,
              height: 140,
              backgroundColor: '#D2691E',
              backgroundImage: 'linear-gradient(135deg, #D2691E 0%, #A0522D 100%)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              borderTopRightRadius: 4,
              borderBottomRightRadius: 4,
              boxShadow: '2px 2px 8px rgba(0,0,0,0.3)',
            }}
          >
            {/* Title decoration */}
            <div
              style={{
                width: 60,
                height: 8,
                backgroundColor: '#FFD700',
                opacity: 0.9,
                marginBottom: 8,
                borderRadius: 1,
              }}
            />
            <div
              style={{
                width: 40,
                height: 6,
                backgroundColor: '#FFD700',
                opacity: 0.7,
                borderRadius: 1,
              }}
            />
          </div>
        </div>
      </div>
    ),
    {
      ...size,
    }
  )
}
