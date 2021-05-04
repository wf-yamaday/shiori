import React, { useEffect, useState } from 'react'
import { useRouter } from 'next/router'
import styles from '../../../styles/Home.module.css'
import { OgpBox } from '../../../components/OgpBox'
import { getBookmarkByIdAsync } from '../../../lib/index'

export default function Details() {
  const router = useRouter()
  const { id } = router.query

  const [bookmark, setBookmark] = useState<any>(undefined);
  const [isLoading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if(!Number(id)) return
    const f = async () => {
      const bookmark = await getBookmarkByIdAsync(Number(id));
      setBookmark(bookmark)
      setLoading(false)
    }
    f();
  }, [id])

  return (
    <div>
      <main className={styles.container}>
        <p>詳細</p>
        {
          isLoading?
          null :
          <div className={styles.content}>
            <OgpBox ogp={bookmark.ogp} />
            <p>memo</p>
            <p>{bookmark.memo}</p>
          </div>
        }
      </main>
    </div>
  )
}
