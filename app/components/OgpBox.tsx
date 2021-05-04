import React, { useCallback, useEffect, useState } from 'react';

interface Props {
  ogp: Object
}

export function OgpBox(props: Props) {
  const ogp = props.ogp;

  return (
    <div className="ogp-box">
      <div className="text">
        <p className="title">{ogp['og:title']}</p>
        {ogp.hasOwnProperty('og:description')? <span className="description">{ogp['og:description']}</span> : null}
      </div>
      {ogp.hasOwnProperty('og:image')? <img className="img" src={ogp['og:image']} /> : null}
    </div>
  )
}
