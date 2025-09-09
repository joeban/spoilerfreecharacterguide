import { ImageResponse } from 'next/og'

export const runtime = 'edge'

export const size = {
  width: 32,
  height: 32,
}

export const contentType = 'image/png'

export default function Icon() {
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
          borderRadius: 6,
        }}
      >
        <div
          style={{
            display: 'flex',
            width: 26,
            height: 20,
            position: 'relative',
          }}
        >
          {/* Book spine */}
          <div
            style={{
              width: 3,
              height: 20,
              backgroundColor: '#8B4513',
              borderTopLeftRadius: 1,
              borderBottomLeftRadius: 1,
            }}
          />
          {/* Book cover */}
          <div
            style={{
              width: 17,
              height: 20,
              backgroundColor: '#D2691E',
              backgroundImage: 'linear-gradient(135deg, #D2691E 0%, #A0522D 100%)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              borderTopRightRadius: 1,
              borderBottomRightRadius: 1,
            }}
          >
            {/* Title decoration */}
            <div
              style={{
                width: 10,
                height: 2,
                backgroundColor: '#FFD700',
                opacity: 0.8,
                marginBottom: 2,
              }}
            />
            <div
              style={{
                width: 7,
                height: 1,
                backgroundColor: '#FFD700',
                opacity: 0.6,
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
