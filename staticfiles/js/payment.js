const confirmPurchase = () => {
    const confirmed = confirm('This will confirm the purchase. Are you sure?');
    if (confirmed) 
        form = document.getElementsByTagName('form')[0].submit();
}