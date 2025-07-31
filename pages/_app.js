// ⚠️ DATA SOURCE INFO
// All character and recap data is stored in /data/*.json.
// - Do NOT regenerate these JSON files unless absolutely necessary.
// - Update existing JSONs to add or edit content.
// - The /data/index.json file lists all series and books.
// - See DATA_README.md in /data for documentation.

import '../styles/globals.css'
import Head from 'next/head'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=EB+Garamond:wght@700&display=swap" rel="stylesheet" />
      </Head>
      <Component {...pageProps} />
    </>
  )
}

export default MyApp
