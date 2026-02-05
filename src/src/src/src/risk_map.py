import folium

def create_risk_map(lat=1.2921, lon=36.8219, risk_score=6.5):  # e.g. Nairobi-ish
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.CircleMarker(
        location=[lat, lon],
        radius=risk_score * 5,
        color='red' if risk_score > 7 else 'orange',
        fill=True,
        fill_color='red',
        popup=f"Water Risk: {risk_score:.1f}/10"
    ).add_to(m)
    m.save('risk_map.html')
    return m

if __name__ == "__main__":
    create_risk_map()
