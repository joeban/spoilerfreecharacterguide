// ⚠️ DATA SOURCE INFO (UPDATED)
// JSON files now use a dictionary-based format.
// - Characters are keyed by name (characters['Vin'])
// - Each character has tiered descriptions in tiers['1-5'] etc.
// - Chapter recaps are in recaps['1']
// See DATA_README.md for examples of the structure.

// ⚠️ DATA SOURCE INFO (UPDATED)
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
